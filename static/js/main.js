// JavaScript for Plant Diagnosis System

document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const diagnosisForm = document.getElementById('diagnosis-form');
    const symptomsInput = document.getElementById('symptoms');
    const resultsSection = document.getElementById('results-section');
    const resultsContainer = document.getElementById('results-container');
    const loadingIndicator = document.getElementById('loading-indicator');
    const newDiagnosisBtn = document.getElementById('new-diagnosis-btn');
    const errorMessage = document.getElementById('error-message');
    const formSection = document.getElementById('form-section');
    
    // Modal Elements
    const keywordsHelpBtn = document.getElementById('keywords-help-btn');
    const keywordsModal = document.getElementById('keywords-modal');
    const closeModalBtn = document.querySelector('.close-modal');
    const closeBtn = document.querySelector('.close-btn');
    
    // Keywords Modal functionality
    if (keywordsHelpBtn && keywordsModal) {
        // Ensure modal is appended to body element for proper positioning
        if (keywordsModal.parentElement !== document.body) {
            document.body.appendChild(keywordsModal);
        }
        
        // Open modal
        keywordsHelpBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            keywordsModal.classList.add('show');
            keywordsModal.classList.remove('hidden');
        });
        
        // Close modal with X button
        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                closeModal();
            });
        }
        
        // Close modal with close button
        if (closeBtn) {
            closeBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                closeModal();
            });
        }
        
        // Close modal function
        function closeModal() {
            keywordsModal.classList.remove('show');
            
            // Use setTimeout to match the CSS transition
            setTimeout(() => {
                keywordsModal.classList.add('hidden');
            }, 300);
        }
        
        // Close when clicking outside the modal content
        document.addEventListener('click', function(e) {
            // If modal is visible and click target is the modal background (not modal content)
            if (!keywordsModal.classList.contains('hidden') && 
                keywordsModal.classList.contains('show') && 
                e.target === keywordsModal) {
                closeModal();
            }
        });
        
        // Add functionality to insert keywords
        const keywordItems = document.querySelectorAll('.keywords-list li');
        keywordItems.forEach(item => {
            item.style.cursor = 'pointer';
            item.title = 'Clique para adicionar ao campo de sintomas';
            
            item.addEventListener('click', function(e) {
                e.stopPropagation();
                const keywordText = this.textContent.trim();
                
                // Get first keyword
                const firstKeyword = keywordText.split(',')[0];
                
                // Insert at cursor position or append
                const currentValue = symptomsInput.value;
                const cursorPos = symptomsInput.selectionStart;
                
                let newValue;
                if (cursorPos !== undefined) {
                    // If there's a cursor position
                    const textBefore = currentValue.substring(0, cursorPos);
                    const textAfter = currentValue.substring(cursorPos);
                    
                    // Add space before keyword if not at beginning and previous char isn't space
                    const spaceBefore = (cursorPos > 0 && textBefore.slice(-1) !== ' ' && textBefore.length > 0) ? ' ' : '';
                    // Add space after keyword if next char isn't space and there is text after
                    const spaceAfter = (textAfter.length > 0 && textAfter[0] !== ' ') ? ' ' : '';
                    
                    newValue = textBefore + spaceBefore + firstKeyword + spaceAfter + textAfter;
                } else {
                    // If no cursor, just append
                    const spaceBefore = currentValue.length > 0 && !currentValue.endsWith(' ') ? ' ' : '';
                    newValue = currentValue + spaceBefore + firstKeyword;
                }
                
                symptomsInput.value = newValue;
                
                // Flash highlight to confirm selection
                item.classList.add('highlight');
                setTimeout(() => item.classList.remove('highlight'), 300);
            });
        });
    }
    
    // Form submission
    if (diagnosisForm) {
        diagnosisForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const symptoms = symptomsInput.value.trim();
            
            // Validate input
            if (symptoms.length < 3) {
                showError('Por favor, descreva os sintomas com mais detalhes (mínimo 3 caracteres).');
                return;
            }
            
            // Clear any previous errors
            hideError();
            
            // Show loading indicator
            showLoading();
            
            // Submit form data
            fetch('/diagnose', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `symptoms=${encodeURIComponent(symptoms)}`
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na comunicação com o servidor');
                }
                return response.json();
            })
            .then(data => {
                hideLoading();
                displayResults(data);
            })
            .catch(error => {
                hideLoading();
                showError(error.message || 'Ocorreu um erro ao processar o diagnóstico.');
            });
        });
    }
    
    // New diagnosis button
    if (newDiagnosisBtn) {
        newDiagnosisBtn.addEventListener('click', function() {
            // Hide results and show form
            resultsSection.classList.add('hidden');
            formSection.classList.remove('hidden');
            
            // Make sure the form itself is visible
            diagnosisForm.classList.remove('hidden');
            
            // Clear form
            if (diagnosisForm) {
                diagnosisForm.reset();
                // Ensure focus on the symptoms input
                symptomsInput.focus();
            }
        });
    }
    
    // Helper functions
    function showLoading() {
        loadingIndicator.classList.remove('hidden');
        diagnosisForm.classList.add('hidden');
    }
    
    function hideLoading() {
        loadingIndicator.classList.add('hidden');
    }
    
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
        
        // Auto-hide error after 5 seconds
        setTimeout(() => {
            hideError();
        }, 5000);
    }
    
    function hideError() {
        errorMessage.classList.add('hidden');
    }
    
    function displayResults(data) {
        // Clear previous results
        resultsContainer.innerHTML = '';
        
        if (data.results && data.results.length > 0) {
            // Create elements for each diagnosis
            data.results.forEach((result, index) => {
                if (index >= 3) return; // Show only top 3 results
                
                const diagnosisItem = document.createElement('div');
                diagnosisItem.className = 'diagnosis-item fade-in';
                diagnosisItem.style.animationDelay = `${index * 0.1}s`;
                
                const relevancePercent = Math.round(result.relevance * 100);
                
                diagnosisItem.innerHTML = `
                    <h3 class="diagnosis-title">
                        ${result.diagnosis}
                        <span class="confidence-badge">Confiança: ${relevancePercent}%</span>
                    </h3>
                    <p class="solution-title">Solução recomendada:</p>
                    <p>${result.solution}</p>
                `;
                
                resultsContainer.appendChild(diagnosisItem);
            });
            
            // Show additional info if there are more than 3 results
            if (data.results.length > 3) {
                const additionalInfo = document.createElement('p');
                additionalInfo.className = 'additional-info';
                additionalInfo.textContent = `* Mais ${data.results.length - 3} diagnósticos possíveis foram identificados com menor relevância.`;
                resultsContainer.appendChild(additionalInfo);
            }
        } else {
            // No results found
            resultsContainer.innerHTML = `
                <div class="no-results fade-in">
                    <h3>Nenhum diagnóstico encontrado</h3>
                    <p>Não foi possível identificar o problema com base nos sintomas fornecidos.</p>
                    <p>Sugestões:</p>
                    <ul>
                        <li>Tente descrever os sintomas de forma mais detalhada.</li>
                        <li>Inclua informações sobre as folhas, caule, flores, etc.</li>
                        <li>Mencione mudanças recentes no ambiente ou nos cuidados com a planta.</li>
                        <li>Use o botão <strong>?</strong> para ver palavras-chave que o sistema reconhece.</li>
                    </ul>
                </div>
            `;
        }
        
        // Show results section
        resultsSection.classList.remove('hidden');
        formSection.classList.add('hidden');
    }
}); 