
        document.getElementById('video-bonus-form').addEventListener('submit', function(event) {
            event.preventDefault();

            fetch(this.action, {
                method: 'POST',
                body: new FormData(this),
                headers: {
                    'Accept': 'application/json'
                }
            }).then(response => {
                if (response.ok) {
                    document.getElementById('video-thank-you-message').style.display = 'block';
                    document.getElementById('video-email-input').value = '';
                    
                    setTimeout(() => {
                        document.getElementById('video-thank-you-message').style.display = 'none';
                    }, 3000);
                } else {
                    alert('Houve um erro ao enviar o e-mail. Por favor, tente novamente.');
                }
            }).catch(error => {
                console.error('Error:', error);
                alert('Houve um erro ao enviar o e-mail. Por favor, tente novamente.');
            });
        });
    