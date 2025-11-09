/**
 * Form Field Enhancer - Transforme les champs texte en listes déroulantes ou cases à cocher
 * ======================================================================================
 * Charge dynamiquement les options depuis l'API et transforme les champs selon la configuration
 */

// Configuration des champs : quel type de contrôle utiliser
const FIELD_CONFIG = {
    // Cases à cocher (choix multiple)
    checkboxes: [
        'antecedents_familiaux',
        'antecedents_personnels',
        'antecedents_chirurgicaux',
        'allergies',
        'traitements_chroniques',
        'petit_dejeuner',
        'dejeuner',
        'diner',
        'grignotage',
        'autres_consommations',
        'asp_resultats',
        'echographie_resultats',
        'topographie_calcul',
        'calcifications_autres'
    ],
    // Listes déroulantes (choix unique)
    selects: [
        'tabac',
        'alcool',
        'forme_calcul',
        'contour_calcul'
    ]
};

let fieldOptions = {};

/**
 * Charge les options de champs depuis l'API
 */
async function loadFieldOptions() {
    try {
        const response = await fetch('/api/field-options');
        if (!response.ok) {
            throw new Error('Erreur lors du chargement des options');
        }
        fieldOptions = await response.json();
        console.log('✓ Options de champs chargées:', Object.keys(fieldOptions).length);
        return fieldOptions;
    } catch (error) {
        console.error('❌ Erreur lors du chargement des options:', error);
        return {};
    }
}

/**
 * Transforme un champ texte en groupe de cases à cocher
 */
function transformToCheckboxes(fieldName, container, label) {
    const options = fieldOptions[fieldName];
    if (!options || options.length === 0) return;

    // Créer le conteneur principal
    const div = document.createElement('div');
    div.className = 'mb-4';
    
    // Créer le label
    const labelElement = document.createElement('label');
    labelElement.className = 'block text-sm font-medium text-gray-700 mb-3';
    labelElement.textContent = label;
    div.appendChild(labelElement);
    
    // Créer le conteneur de grille pour les checkboxes
    const gridContainer = document.createElement('div');
    gridContainer.className = 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 p-4 bg-gray-50 border border-gray-200 rounded-lg max-h-80 overflow-y-auto';
    
    // Créer les checkboxes
    options.forEach((option, index) => {
        const checkboxDiv = document.createElement('div');
        checkboxDiv.className = 'flex items-center';
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = `${fieldName}_option`;
        checkbox.value = option;
        checkbox.id = `${fieldName}_${index}`;
        checkbox.className = 'mr-2 h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded';
        
        const checkboxLabel = document.createElement('label');
        checkboxLabel.htmlFor = `${fieldName}_${index}`;
        checkboxLabel.className = 'text-sm text-gray-700 cursor-pointer';
        checkboxLabel.textContent = option;
        
        checkboxDiv.appendChild(checkbox);
        checkboxDiv.appendChild(checkboxLabel);
        gridContainer.appendChild(checkboxDiv);
    });
    
    div.appendChild(gridContainer);
    
    // Créer un champ texte caché pour les données additionnelles
    const additionalInput = document.createElement('textarea');
    additionalInput.name = `${fieldName}_additional`;
    additionalInput.placeholder = 'Informations complémentaires (facultatif)...';
    additionalInput.className = 'mt-2 input-field';
    additionalInput.rows = 2;
    div.appendChild(additionalInput);
    
    // Remplacer le container original
    container.innerHTML = '';
    container.appendChild(div);
    
    // Ajouter un champ caché pour stocker la valeur combinée
    const hiddenInput = document.createElement('input');
    hiddenInput.type = 'hidden';
    hiddenInput.name = fieldName;
    hiddenInput.id = `${fieldName}_combined`;
    container.appendChild(hiddenInput);
    
    // Fonction pour mettre à jour le champ caché
    function updateCombinedValue() {
        const selectedOptions = Array.from(gridContainer.querySelectorAll('input[type="checkbox"]:checked'))
            .map(cb => cb.value);
        const additional = additionalInput.value.trim();
        
        let combinedValue = selectedOptions.join('; ');
        if (additional && additional.length > 0) {
            combinedValue += (combinedValue ? '; ' : '') + additional;
        }
        
        hiddenInput.value = combinedValue;
    }
    
    // Écouter les changements
    gridContainer.addEventListener('change', updateCombinedValue);
    additionalInput.addEventListener('input', updateCombinedValue);
}

/**
 * Transforme un champ texte en liste déroulante
 */
function transformToSelect(fieldName, originalInput, label) {
    const options = fieldOptions[fieldName];
    if (!options || options.length === 0) return;

    // Créer le select
    const select = document.createElement('select');
    select.name = fieldName;
    select.id = fieldName;
    select.className = originalInput.className;
    
    // Ajouter les options
    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        select.appendChild(optionElement);
    });
    
    // Remplacer l'input original
    originalInput.parentNode.replaceChild(select, originalInput);
}

/**
 * Parse une valeur existante (point-virgule séparé) en cases cochées
 */
function parseAndCheckExistingValue(fieldName, value) {
    if (!value) return;
    
    const values = value.split(';').map(v => v.trim()).filter(v => v);
    const checkboxes = document.querySelectorAll(`input[name="${fieldName}_option"]`);
    
    checkboxes.forEach(checkbox => {
        if (values.includes(checkbox.value)) {
            checkbox.checked = true;
        }
    });
    
    // Mettre à jour le champ caché
    const hiddenInput = document.getElementById(`${fieldName}_combined`);
    if (hiddenInput) {
        hiddenInput.value = value;
    }
}

/**
 * Initialise les transformations de champs
 */
async function initializeFormEnhancements() {
    console.log('🔧 Initialisation des améliorations de formulaire...');
    
    // Charger les options
    await loadFieldOptions();
    
    // Transformer les champs en checkboxes
    FIELD_CONFIG.checkboxes.forEach(fieldName => {
        // Trouver le conteneur du champ (div parent de l'input)
        let container = null;
        let label = '';
        
        // Chercher par différentes méthodes
        const inputByName = document.querySelector(`input[name="${fieldName}"], textarea[name="${fieldName}"]`);
        if (inputByName) {
            container = inputByName.closest('.mb-4, div');
            const labelElement = container?.querySelector('label');
            if (labelElement) {
                label = labelElement.textContent.trim();
            }
        }
        
        if (container && fieldOptions[fieldName]) {
            const existingValue = inputByName?.value || '';
            transformToCheckboxes(fieldName, container, label || fieldName);
            
            // Si une valeur existait, la parser
            if (existingValue) {
                setTimeout(() => parseAndCheckExistingValue(fieldName, existingValue), 100);
            }
        }
    });
    
    // Transformer les champs en selects
    FIELD_CONFIG.selects.forEach(fieldName => {
        const originalInput = document.querySelector(`input[name="${fieldName}"], select[name="${fieldName}"]`);
        if (originalInput && fieldOptions[fieldName]) {
            const labelElement = originalInput.previousElementSibling;
            const label = labelElement?.textContent || fieldName;
            
            // Ne transformer que si c'est un input (pas déjà un select)
            if (originalInput.tagName.toLowerCase() === 'input') {
                transformToSelect(fieldName, originalInput, label);
            }
        }
    });
    
    console.log('✅ Améliorations de formulaire initialisées');
}

// Initialiser au chargement de la page
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeFormEnhancements);
} else {
    initializeFormEnhancements();
}
