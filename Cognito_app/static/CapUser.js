document.getElementById('take-photo-button').addEventListener('click', function() {
    
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // Peça permissão para acessar a câmera
      navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        // Crie um elemento de vídeo e adicione a stream da câmera nele
        var videoElement = document.createElement('video');
        videoElement.srcObject = stream;
        videoElement.addEventListener('loadedmetadata', function() {
          // Quando o vídeo estiver pronto, crie um canvas e um contexto 2D nele
          var canvas = document.createElement('canvas');
          var context = canvas.getContext('2d');
  
          canvas.width = videoElement.videoWidth;
          canvas.height = videoElement.videoHeight;
  
          context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
  
          // Converta o conteúdo do canvas em uma imagem em formato JPEG
          var imageData = canvas.toDataURL('image/jpeg');
  
          // Envie a imagem para o Django
          uploadToDjango(imageData);
        });
      });
    }
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
  
  function uploadToDjango(imageData) {
    const csrftoken = getCookie('csrftoken');
    var user_name = document.getElementById('email').value
    
    // enviar a imagem para o Django
    fetch('/registration/', {
      method: 'POST',
      body: [imageData,user_name],
      headers: { "X-CSRFToken": csrftoken }
    }).then(function(response) {
      Swal.fire({
        position: 'top',
        icon: 'success',
        title: `Sucesso!`,
        text: `${user_name} cadastrado com sucesso!`,
        showConfirmButton: false,
        timer: 2500
      })
    }).catch(function(error) {
      console.log('Error uploading image:', error);
  });
  }



  //if para n permitir reenvio de formulario 
if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
  }
  