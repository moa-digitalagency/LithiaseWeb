function calculerIMC() {
    const poids = parseFloat(document.getElementById('poids').value);
    const taille = parseFloat(document.getElementById('taille').value);
    const imcField = document.getElementById('imc');
    
    if (poids > 0 && taille > 0) {
        const tailleMetres = taille / 100;
        const imc = (poids / (tailleMetres * tailleMetres)).toFixed(1);
        imcField.value = imc + ' kg/m²';
        
        if (imc < 18.5) {
            imcField.className = 'input-field bg-blue-100 text-blue-800 font-semibold';
        } else if (imc < 25) {
            imcField.className = 'input-field bg-green-100 text-green-800 font-semibold';
        } else if (imc < 30) {
            imcField.className = 'input-field bg-yellow-100 text-yellow-800 font-semibold';
        } else {
            imcField.className = 'input-field bg-red-100 text-red-800 font-semibold';
        }
    } else {
        imcField.value = '--';
        imcField.className = 'input-field bg-gray-100';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('poids').addEventListener('input', calculerIMC);
    document.getElementById('taille').addEventListener('input', calculerIMC);
    
    document.getElementById('newPatientForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const data = {};
        
        for (let [key, value] of formData.entries()) {
            if (value instanceof File) {
                continue;
            }
            if (value !== '') {
                data[key] = value;
            }
        }
        
        try {
            const response = await fetch('/api/patients', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                const result = await response.json();
                alert('✓ Patient créé avec succès!');
                window.location.href = '/patient/' + result.id;
            } else {
                const error = await response.json();
                alert('❌ Erreur lors de la création du patient: ' + (error.error || 'Erreur inconnue'));
            }
        } catch (error) {
            alert('❌ Erreur de connexion au serveur');
            console.error('Error:', error);
        }
    });
});
