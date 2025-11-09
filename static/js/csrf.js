function getCSRFToken() {
    const tokenMeta = document.querySelector('meta[name="csrf-token"]');
    return tokenMeta ? tokenMeta.getAttribute('content') : '';
}

function fetchWithCSRF(url, options = {}) {
    const token = getCSRFToken();
    
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        credentials: 'same-origin'
    };
    
    const mergedOptions = {
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...(options.headers || {})
        }
    };
    
    return fetch(url, mergedOptions);
}
