const uploadBtn = document.getElementById('uploadBtn');
const videoInput = document.getElementById('videoInput');
const videoContainer = document.getElementById('video-container');
const videoElement = document.getElementById('video');
const captionDisplay = document.getElementById('caption-display');
const summaryText = document.getElementById('summary-text');

uploadBtn.addEventListener('click', async () => {
  const file = videoInput.files[0];
  if (!file) {
    alert("Please choose a video first!");
    return;
  }

  const formData = new FormData();
  formData.append('video', file);

  uploadBtn.textContent = "Processing...";
  uploadBtn.disabled = true;

  const response = await fetch('/upload', {
    method: 'POST',
    body: formData
  });

  const data = await response.json();
  uploadBtn.textContent = "Upload & Generate";
  uploadBtn.disabled = false;

  if (data.error) {
    alert(data.error);
    return;
  }

  // Show video
  videoContainer.style.display = "block";
  videoElement.src = data.video_path;

  // Show summary
  summaryText.textContent = data.paragraph;

  const captions = data.captions;

  // Live captions sync
  videoElement.addEventListener('timeupdate', () => {
    const current = captions.find(
      c => videoElement.currentTime >= c.start && videoElement.currentTime <= c.end
    );
    captionDisplay.textContent = current ? current.text : "";
  });
});
