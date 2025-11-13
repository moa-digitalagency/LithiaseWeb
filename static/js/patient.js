let currentEpisodeId = null;

async function loadPatient() {
    const patientId = window.patientId;
    const response = await fetch(`/api/patients/${patientId}`);
    const patient = await response.json();
    
    document.getElementById('patientName').textContent = `👤 ${patient.nom} ${patient.prenom}`;
    
    const bmi = patient.poids && patient.taille ? (patient.poids / Math.pow(patient.taille / 100, 2)).toFixed(1) : null;
    
    const calculateAge = (birthDate) => {
        if (!birthDate) return null;
        const today = new Date();
        const birth = new Date(birthDate);
        if (isNaN(birth.getTime())) return null;
        let age = today.getFullYear() - birth.getFullYear();
        const monthDiff = today.getMonth() - birth.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
            age--;
        }
        return age;
    };
    
    const age = calculateAge(patient.date_naissance);
    
    document.getElementById('patientInfo').innerHTML = `
        <div class="info-card"><strong>👤 Nom complet:</strong> ${patient.nom} ${patient.prenom}</div>
        ${age !== null ? `<div class="info-card"><strong>🎂 Âge:</strong> ${age} ans</div>` : ''}
        ${patient.poids ? `<div class="info-card"><strong>⚖️ Poids:</strong> ${patient.poids} kg</div>` : ''}
        ${patient.taille ? `<div class="info-card"><strong>📏 Taille:</strong> ${patient.taille} cm</div>` : ''}
        ${bmi ? `<div class="info-card"><strong>📊 IMC:</strong> ${bmi}</div>` : ''}
        <div class="info-card"><strong>📞 Téléphone:</strong> ${patient.telephone || '-'}</div>
        <div class="info-card"><strong>📧 Email:</strong> ${patient.email || '-'}</div>
        ${patient.groupe_ethnique ? `<div class="info-card"><strong>🌍 Groupe ethnique:</strong> ${patient.groupe_ethnique}</div>` : ''}
        ${patient.adresse ? `<div class="info-card col-span-2"><strong>📍 Adresse:</strong> ${patient.adresse}</div>` : ''}
    `;
    
    document.getElementById('patientMedicalHistory').innerHTML = `
        ${patient.antecedents_personnels ? `<div class="info-card"><strong>📋 Antécédents personnels:</strong> ${patient.antecedents_personnels}</div>` : ''}
        ${patient.antecedents_familiaux ? `<div class="info-card"><strong>👨‍👩‍👧‍👦 Antécédents familiaux:</strong> ${patient.antecedents_familiaux}</div>` : ''}
        ${patient.antecedents_chirurgicaux ? `<div class="info-card"><strong>🏥 Antécédents chirurgicaux:</strong> ${patient.antecedents_chirurgicaux}</div>` : ''}
        ${patient.allergies ? `<div class="info-card"><strong>⚠️ Allergies:</strong> ${patient.allergies}</div>` : ''}
        ${patient.traitements_chroniques ? `<div class="info-card"><strong>💊 Traitements chroniques:</strong> ${patient.traitements_chroniques}</div>` : ''}
    `;
    
    const dietaryHabitsHTML = [];
    if (patient.petit_dejeuner) dietaryHabitsHTML.push(`<div class="info-card"><strong>🌅 Petit déjeuner:</strong> ${patient.petit_dejeuner}</div>`);
    if (patient.dejeuner) dietaryHabitsHTML.push(`<div class="info-card"><strong>☀️ Déjeuner:</strong> ${patient.dejeuner}</div>`);
    if (patient.diner) dietaryHabitsHTML.push(`<div class="info-card"><strong>🌙 Dîner:</strong> ${patient.diner}</div>`);
    if (patient.grignotage) dietaryHabitsHTML.push(`<div class="info-card"><strong>🍪 Grignotage:</strong> ${patient.grignotage}</div>`);
    if (patient.autres_consommations) dietaryHabitsHTML.push(`<div class="info-card"><strong>🍷 Autres consommations:</strong> ${patient.autres_consommations}</div>`);
    
    document.getElementById('patientRiskFactors').innerHTML = `
        ${patient.hydratation_jour ? `<div class="info-card"><strong>💧 Hydratation:</strong> ${patient.hydratation_jour} L/jour</div>` : ''}
        ${patient.regime_alimentaire ? `<div class="info-card col-span-2"><strong>🍽️ Régime alimentaire:</strong> ${patient.regime_alimentaire}</div>` : ''}
        ${dietaryHabitsHTML.length > 0 ? '<div class="col-span-2 border-t pt-3 mt-3"><h4 class="font-semibold text-gray-800 mb-2">🍴 Habitudes alimentaires détaillées</h4></div>' : ''}
        ${dietaryHabitsHTML.join('')}
    `;
    
    if (patient.notes) {
        document.getElementById('patientNotesSection').classList.remove('hidden');
        document.getElementById('patientNotes').textContent = patient.notes;
    }
    
    loadEpisodes();
}

async function loadEpisodes() {
    const patientId = window.patientId;
    const response = await fetch(`/api/patients/${patientId}/episodes`);
    const episodes = await response.json();
    
    const container = document.getElementById('episodesList');
    
    if (episodes.length === 0) {
        container.innerHTML = '<p class="text-gray-500 text-center py-8">😔 Aucun épisode enregistré</p>';
        return;
    }
    
    container.innerHTML = episodes.map(e => `
        <div class="episode-card" onclick="showEpisodeDetail(${e.id})">
            <div class="flex justify-between">
                <div>
                    <h4 class="font-semibold text-lg text-gray-800">📋 ${e.motif || 'Épisode'}</h4>
                    <p class="text-gray-600 text-sm mt-1">📅 ${new Date(e.date_episode).toLocaleDateString('fr-FR')}</p>
                    <p class="text-gray-700 text-sm mt-1">${e.diagnostic || ''}</p>
                </div>
                <div class="flex flex-col gap-2 text-sm">
                    <span class="badge badge-info">🔬 ${e.nb_imageries} imagerie(s)</span>
                    <span class="badge badge-success">🧪 ${e.nb_biologies} biologie(s)</span>
                </div>
            </div>
        </div>
    `).join('');
}

async function showEpisodeDetail(episodeId) {
    currentEpisodeId = episodeId;
    const response = await fetch(`/api/episodes/${episodeId}`);
    const episode = await response.json();
    
    document.getElementById('imagingList').innerHTML = episode.imageries.map(i => `
        <div class="info-card">
            <div><strong>📅 Date:</strong> ${new Date(i.date_examen).toLocaleDateString('fr-FR')}</div>
            ${i.asp_resultats ? `<div class="col-span-2"><strong>📋 ASP:</strong> ${i.asp_resultats}</div>` : ''}
            ${i.echographie_resultats ? `<div class="col-span-2"><strong>🔊 Échographie:</strong> ${i.echographie_resultats}</div>` : ''}
            ${i.uroscanner_resultats ? `<div class="col-span-2"><strong>💻 Uro-scanner:</strong> ${i.uroscanner_resultats}</div>` : ''}
            ${i.nombre_calculs ? `<div><strong>🔢 Nombre de calculs:</strong> ${i.nombre_calculs}</div>` : ''}
            ${i.topographie_calcul ? `<div><strong>📍 Topographie:</strong> ${i.topographie_calcul}</div>` : ''}
            ${i.diametre_longitudinal ? `<div><strong>📏 Diam. longitudinal:</strong> ${i.diametre_longitudinal} mm</div>` : ''}
            ${i.diametre_transversal ? `<div><strong>📐 Diam. transversal:</strong> ${i.diametre_transversal} mm</div>` : ''}
            ${i.taille_mm ? `<div><strong>📏 Taille:</strong> ${i.taille_mm} mm</div>` : ''}
            ${i.forme_calcul ? `<div><strong>🔶 Forme:</strong> ${i.forme_calcul}</div>` : ''}
            ${i.contour_calcul ? `<div><strong>⭕ Contour:</strong> ${i.contour_calcul}</div>` : ''}
            ${i.densite_noyau ? `<div><strong>💎 Densité noyau:</strong> ${i.densite_noyau} UH</div>` : ''}
            ${i.densites_couches ? `<div class="col-span-2"><strong>🌈 Densités couches:</strong> ${i.densites_couches}</div>` : ''}
            ${i.morphologie ? `<div><strong>🔍 Morphologie:</strong> ${i.morphologie}</div>` : ''}
            ${i.radio_opacite ? `<div><strong>📡 Radio-opacité:</strong> ${i.radio_opacite}</div>` : ''}
            ${i.localisation ? `<div class="col-span-2"><strong>📌 Localisation:</strong> ${i.localisation}</div>` : ''}
            ${i.calcifications_autres ? `<div class="col-span-2"><strong>🧮 Autres calcifications:</strong> ${i.calcifications_autres}</div>` : ''}
        </div>
    `).join('') || '<p class="text-gray-500">😔 Aucune imagerie</p>';
    
    document.getElementById('biologyList').innerHTML = episode.biologies.map(b => `
        <div class="info-card">
            <div><strong>📅 Date:</strong> ${new Date(b.date_examen).toLocaleDateString('fr-FR')}</div>
            ${b.ph_urinaire ? `<div><strong>🧪 pH urinaire:</strong> ${b.ph_urinaire}</div>` : ''}
            ${b.densite_urinaire ? `<div><strong>💧 Densité urinaire:</strong> ${b.densite_urinaire}</div>` : ''}
            ${b.sediment_urinaire ? `<div class="col-span-2"><strong>🔬 Sédiment urinaire:</strong> ${b.sediment_urinaire}</div>` : ''}
            ${b.ecbu_resultats ? `<div class="col-span-2"><strong>🦠 ECBU:</strong> ${b.ecbu_resultats}</div>` : ''}
            <div class="col-span-2 mt-2 border-t pt-2">
                <strong>📊 Marqueurs métaboliques:</strong>
                <div class="grid grid-cols-2 gap-2 mt-1">
                    <span>Hyperoxalurie: ${b.hyperoxalurie ? '✅' : '❌'} ${b.oxalurie_valeur ? `(${b.oxalurie_valeur} mg/24h)` : ''}</span>
                    <span>Hypercalciurie: ${b.hypercalciurie ? '✅' : '❌'} ${b.calciurie_valeur ? `(${b.calciurie_valeur} mg/24h)` : ''}</span>
                    <span>Hyperuricurie: ${b.hyperuricurie ? '✅' : '❌'}</span>
                    <span>Cystinurie: ${b.cystinurie ? '✅' : '❌'}</span>
                    <span>Hypercalcémie: ${b.hypercalcemie ? '✅' : '❌'} ${b.calciemie_valeur ? `(${b.calciemie_valeur} mmol/L)` : ''}</span>
                </div>
            </div>
            ${(b.t3 || b.t4 || b.tsh) ? `<div class="col-span-2 mt-2 border-t pt-2">
                <strong>🦋 Hormones thyroïdiennes:</strong>
                <div class="grid grid-cols-3 gap-2 mt-1">
                    ${b.tsh !== null && b.tsh !== undefined ? `<span>TSH: ${b.tsh} mUI/L</span>` : ''}
                    ${b.t3 ? `<span>T3: ${b.t3} pg/mL</span>` : ''}
                    ${b.t4 ? `<span>T4: ${b.t4} ng/dL</span>` : ''}
                </div>
            </div>` : ''}
            ${b.infection_urinaire ? `<div class="col-span-2 mt-2"><strong>🦠 Infection:</strong> Oui ${b.germe ? `(${b.germe})` : ''}</div>` : ''}
        </div>
    `).join('') || '<p class="text-gray-500">😔 Aucune biologie</p>';
    
    if (episode.calculated_data) {
        displayInferenceResult(episode.calculated_data);
    }
    
    document.getElementById('episodeDetailModal').classList.remove('hidden');
}

function displayInferenceResult(result) {
    document.getElementById('inferenceResult').innerHTML = `
        <div style="border: 2px dashed #8B5CF6; background: rgba(139, 92, 246, 0.08); border-radius: 1.5rem; padding: 2rem;">
            <h4 class="text-2xl font-bold mb-4" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🧮 Résultat de l'inférence</h4>
            
            ${result.uncertain ? '<div style="background: rgba(245, 158, 11, 0.08); border: 2px solid #F59E0B; color: #92400E; padding: 0.75rem 1rem; border-radius: 1rem; margin-bottom: 1rem;">⚠️ Résultat incertain, compléter biologie/CT</div>' : ''}
            
            <div class="mb-4 p-4 rounded-lg" style="background: ${result.composition_type === 'Pur' ? 'rgba(34, 197, 94, 0.1)' : 'rgba(249, 115, 22, 0.1)'}; border: 2px solid ${result.composition_type === 'Pur' ? '#22C55E' : '#F97316'};">
                <h5 class="font-bold text-xl mb-2">🎯 Nature morpho-constitutionnelle</h5>
                <p class="text-lg font-semibold mb-1" style="color: ${result.composition_type === 'Pur' ? '#15803D' : '#C2410C'};">
                    ${result.composition_type === 'Pur' ? '💎' : '🔀'} ${result.composition_detail}
                </p>
                <p class="text-gray-700 text-sm">⭐ Score: ${result.top_1_score}/20</p>
            </div>
            
            <div class="mb-4">
                <h5 class="font-semibold mb-2">📝 Justification:</h5>
                <ul class="list-disc list-inside space-y-1">
                    ${result.top_1_reasons.map(r => `<li class="text-gray-700">${r}</li>`).join('')}
                </ul>
            </div>
            
            <div class="mb-4">
                <h5 class="font-semibold mb-2">📊 Top 3:</h5>
                ${result.top_3.map(([type, score]) => `<div class="flex justify-between py-1 px-2 bg-white rounded"><span>${type}</span><span class="font-mono font-bold">${score}/20</span></div>`).join('')}
            </div>
            
            <div class="grid grid-cols-2 gap-4 mb-4">
                <div class="bg-white p-3 rounded-lg">
                    <strong>⚡ LEC éligible:</strong> <span class="font-semibold ${result.lec_eligible ? 'text-green-600' : 'text-red-600'}">${result.lec_eligible ? '✅ Oui' : '❌ Non'}</span>
                </div>
                <div class="bg-white p-3 rounded-lg">
                    <strong>🔬 Voie de traitement:</strong> ${result.voie_traitement}
                </div>
            </div>
            
            <div class="bg-white p-4 rounded-lg">
                <h5 class="font-semibold mb-2">🛡️ Prévention:</h5>
                <ul class="list-disc list-inside space-y-1">
                    ${result.prevention.map(p => `<li class="text-gray-700">${p}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;
}

async function runInference() {
    const response = await fetchWithCSRF(`/api/episodes/${currentEpisodeId}/inference`, {
        method: 'POST'
    });
    const result = await response.json();
    
    if (result.error) {
        document.getElementById('inferenceResult').innerHTML = `<div style="background: rgba(239, 68, 68, 0.08); border: 2px solid #EF4444; color: #991B1B; padding: 1rem; border-radius: 1rem;">❌ ${result.error}</div>`;
        return;
    }
    
    displayInferenceResult(result);
}

function showNewEpisodeModal() {
    document.getElementById('newEpisodeModal').classList.remove('hidden');
}

function hideNewEpisodeModal() {
    document.getElementById('newEpisodeModal').classList.add('hidden');
}

function hideEpisodeDetailModal() {
    document.getElementById('episodeDetailModal').classList.add('hidden');
    document.getElementById('inferenceResult').innerHTML = '';
}

function showNewImagingModal() {
    document.getElementById('newImagingModal').classList.remove('hidden');
}

function hideNewImagingModal() {
    document.getElementById('newImagingModal').classList.add('hidden');
}

function showNewBiologyModal() {
    document.getElementById('newBiologyModal').classList.remove('hidden');
}

function hideNewBiologyModal() {
    document.getElementById('newBiologyModal').classList.add('hidden');
}

async function exportPDF() {
    const patientId = window.patientId;
    window.open(`/api/patients/${patientId}/export/pdf`, '_blank');
}

async function showEditPatientModal() {
    const patientId = window.patientId;
    const response = await fetch(`/api/patients/${patientId}`);
    const patient = await response.json();
    
    document.getElementById('edit_nom').value = patient.nom || '';
    document.getElementById('edit_prenom').value = patient.prenom || '';
    document.getElementById('edit_groupe_ethnique').value = patient.groupe_ethnique || '';
    document.getElementById('edit_telephone').value = patient.telephone || '';
    document.getElementById('edit_email').value = patient.email || '';
    document.getElementById('edit_adresse').value = patient.adresse || '';
    document.getElementById('edit_poids').value = patient.poids || '';
    document.getElementById('edit_taille').value = patient.taille || '';
    
    document.getElementById('edit_antecedents_personnels').value = patient.antecedents_personnels || '';
    document.getElementById('edit_antecedents_familiaux').value = patient.antecedents_familiaux || '';
    document.getElementById('edit_antecedents_chirurgicaux').value = patient.antecedents_chirurgicaux || '';
    document.getElementById('edit_allergies').value = patient.allergies || '';
    document.getElementById('edit_traitements_chroniques').value = patient.traitements_chroniques || '';
    
    document.getElementById('edit_hydratation_jour').value = patient.hydratation_jour || '';
    document.getElementById('edit_regime_alimentaire').value = patient.regime_alimentaire || '';
    document.getElementById('edit_petit_dejeuner').value = patient.petit_dejeuner || '';
    document.getElementById('edit_dejeuner').value = patient.dejeuner || '';
    document.getElementById('edit_diner').value = patient.diner || '';
    document.getElementById('edit_grignotage').value = patient.grignotage || '';
    document.getElementById('edit_autres_consommations').value = patient.autres_consommations || '';
    
    document.getElementById('edit_asp_resultats').value = patient.asp_resultats || '';
    document.getElementById('edit_echographie_resultats').value = patient.echographie_resultats || '';
    document.getElementById('edit_uroscanner_resultats').value = patient.uroscanner_resultats || '';
    document.getElementById('edit_nombre_calculs').value = patient.nombre_calculs || '';
    document.getElementById('edit_topographie_calcul').value = patient.topographie_calcul || '';
    document.getElementById('edit_diametre_longitudinal').value = patient.diametre_longitudinal || '';
    document.getElementById('edit_diametre_transversal').value = patient.diametre_transversal || '';
    document.getElementById('edit_forme_calcul').value = patient.forme_calcul || '';
    document.getElementById('edit_contour_calcul').value = patient.contour_calcul || '';
    document.getElementById('edit_densite_noyau').value = patient.densite_noyau || '';
    document.getElementById('edit_densites_couches').value = patient.densites_couches || '';
    document.getElementById('edit_calcifications_autres').value = patient.calcifications_autres || '';
    document.getElementById('edit_sediment_urinaire').value = patient.sediment_urinaire || '';
    document.getElementById('edit_ecbu_resultats').value = patient.ecbu_resultats || '';
    document.getElementById('edit_ph_urinaire').value = patient.ph_urinaire || '';
    document.getElementById('edit_densite_urinaire').value = patient.densite_urinaire || '';
    
    document.getElementById('edit_notes').value = patient.notes || '';
    
    document.getElementById('editPatientModal').classList.remove('hidden');
}

function hideEditPatientModal() {
    document.getElementById('editPatientModal').classList.add('hidden');
}

function showDeleteConfirmModal() {
    document.getElementById('deleteConfirmModal').classList.remove('hidden');
}

function hideDeleteConfirmModal() {
    document.getElementById('deleteConfirmModal').classList.add('hidden');
}

async function deletePatient() {
    const patientId = window.patientId;
    const response = await fetchWithCSRF(`/api/patients/${patientId}`, {
        method: 'DELETE'
    });
    
    if (response.ok) {
        window.location.href = '/';
    } else {
        alert('Erreur lors de la suppression du patient');
        hideDeleteConfirmModal();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    ['newEpisodeModal', 'episodeDetailModal', 'newImagingModal', 'newBiologyModal'].forEach(modalId => {
        document.getElementById(modalId).addEventListener('click', (e) => {
            if (e.target.id === modalId) {
                document.getElementById(modalId).classList.add('hidden');
            }
        });
    });
    
    document.getElementById('newEpisodeForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const patientId = window.patientId;
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData.entries());
        data.douleur = formData.has('douleur');
        data.fievre = formData.has('fievre');
        data.infection_urinaire = formData.has('infection_urinaire');
        
        await fetchWithCSRF(`/api/patients/${patientId}/episodes`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
        
        hideNewEpisodeModal();
        loadEpisodes();
    });
    
    document.getElementById('newImagingForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData.entries());
        
        await fetchWithCSRF(`/api/episodes/${currentEpisodeId}/imageries`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
        
        hideNewImagingModal();
        showEpisodeDetail(currentEpisodeId);
    });
    
    document.getElementById('newBiologyForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData.entries());
        data.hyperuricurie = formData.has('hyperuricurie');
        data.cystinurie = formData.has('cystinurie');
        data.infection_urinaire = formData.has('infection_urinaire');
        
        if (data.oxalurie_valeur) data.oxalurie_valeur = parseFloat(data.oxalurie_valeur);
        if (data.calciurie_valeur) data.calciurie_valeur = parseFloat(data.calciurie_valeur);
        if (data.calciemie_valeur) data.calciemie_valeur = parseFloat(data.calciemie_valeur);
        if (data.tsh) data.tsh = parseFloat(data.tsh);
        if (data.t3) data.t3 = parseFloat(data.t3);
        if (data.t4) data.t4 = parseFloat(data.t4);
        
        await fetchWithCSRF(`/api/episodes/${currentEpisodeId}/biologies`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
        
        hideNewBiologyModal();
        showEpisodeDetail(currentEpisodeId);
    });
    
    document.getElementById('editPatientForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const patientId = window.patientId;
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData.entries());
        
        const response = await fetchWithCSRF(`/api/patients/${patientId}`, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            hideEditPatientModal();
            loadPatient();
        } else {
            alert('Erreur lors de la modification du patient');
        }
    });
    
    ['editPatientModal', 'deleteConfirmModal'].forEach(modalId => {
        document.getElementById(modalId).addEventListener('click', (e) => {
            if (e.target.id === modalId) {
                document.getElementById(modalId).classList.add('hidden');
            }
        });
    });
    
    loadPatient();
});
