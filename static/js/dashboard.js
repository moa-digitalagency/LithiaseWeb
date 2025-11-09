async function loadPatients(search = '') {
    const response = await fetch(`/api/patients?search=${search}`);
    const patients = await response.json();
    
    updateStatistics(patients);
    
    const container = document.getElementById('patientsList');
    
    if (patients.length === 0) {
        container.innerHTML = '<p class="text-gray-500 text-center py-8">😔 Aucun patient trouvé</p>';
        return;
    }
    
    container.innerHTML = patients.map(p => `
        <div class="patient-card"
             onclick="window.location.href='/patient/${p.id}'">
            <div class="flex justify-between items-start">
                <div>
                    <h3 class="text-lg font-semibold text-gray-800">👤 ${p.nom} ${p.prenom}</h3>
                    <p class="text-gray-600 text-sm mt-1">📅 Né(e) le ${new Date(p.date_naissance).toLocaleDateString('fr-FR')}</p>
                    <p class="text-gray-600 text-sm">📞 ${p.telephone || 'Téléphone non renseigné'}</p>
                </div>
                <div class="text-right">
                    <span class="badge badge-info">
                        📊 ${p.nb_episodes} épisode(s)
                    </span>
                </div>
            </div>
        </div>
    `).join('');
}

async function updateStatistics(patients) {
    document.getElementById('totalPatients').textContent = patients.length;
    
    const totalEpisodes = patients.reduce((sum, p) => sum + (p.nb_episodes || 0), 0);
    document.getElementById('totalEpisodes').textContent = totalEpisodes;
    
    const patientsWithBMI = await Promise.all(
        patients.map(async p => {
            const detailResponse = await fetch(`/api/patients/${p.id}`);
            return detailResponse.json();
        })
    );
    
    const validBMIs = patientsWithBMI
        .filter(p => p.poids && p.taille)
        .map(p => p.poids / Math.pow(p.taille / 100, 2));
    
    if (validBMIs.length > 0) {
        const avgBMI = validBMIs.reduce((a, b) => a + b, 0) / validBMIs.length;
        document.getElementById('avgBMI').textContent = avgBMI.toFixed(1);
    } else {
        document.getElementById('avgBMI').textContent = '-';
    }
    
    let hypercalciuriaCount = 0;
    for (const patient of patientsWithBMI) {
        const episodesResponse = await fetch(`/api/patients/${patient.id}/episodes`);
        const episodes = await episodesResponse.json();
        
        for (const episode of episodes) {
            if (episode.biologies && episode.biologies.length > 0) {
                const hasHypercalciuria = episode.biologies.some(b => b.hypercalciurie);
                if (hasHypercalciuria) {
                    hypercalciuriaCount++;
                    break;
                }
            }
        }
    }
    document.getElementById('hypercalciuriaCount').textContent = hypercalciuriaCount;
    
    const aiReadyCount = patientsWithBMI.filter(p => 
        p.poids && p.taille && (p.petit_dejeuner || p.dejeuner || p.diner)
    ).length;
    document.getElementById('aiDataCount').textContent = aiReadyCount;
}

function searchPatients() {
    const search = document.getElementById('searchInput').value;
    loadPatients(search);
}

document.addEventListener('DOMContentLoaded', () => {
    loadPatients();
});
