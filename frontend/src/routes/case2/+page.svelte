<script>
  import Loading from "./loading.svelte";
  let files;
  let imageUrls = [];
  let status = 0;
  const uploadFiles = async () => {
    status = -1;
    if (!files || files.length === 0) {
      console.error('No files selected');
      return;
    }

    for (let file of files) {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const filename = await response.text();
        imageUrls.push(`http://localhost:5000/all_images/${filename}`);
        console.log('File uploaded successfully');
      } else {
        console.error('File upload failed');
      }
    }

    const scriptResponse = await fetch('http://localhost:5000/run_script', {
      method: 'POST',
    });

    if (scriptResponse.ok) {
      console.log('Script executed successfully');
    } else {
      console.error('Script execution failed');
    }
    status = 0;
  };

  function repeat() {
    imageUrls = [];
    status = 1;
  }
</script>







  <div style = "height:980px;" class = "w-full flex flex-col items-center">
  <h1 class="dark:text-white text-9xl mt-10 madimi mb-20 pb-20">Deforestation Analysis</h1>
  
  {#if status == 0}
  <div class = "flex flex-row">
    <img src = "./solution/deforestation1.png" width=900>
    <img src = "./solution/deforestation2.png" width=900>
  </div>
    <button on:click={repeat} class="cu text-3xl bg-slate-300 dark:bg-slate-500 dark:hover:bg-blue-500 hover:bg-blue-300 rounded-md p-4 madimi dark:text-white mt-10">Try Again</button>
    {:else if status == -1}
    <Loading />
  {:else}
    <label for="file" class="custom-file-label text-4xl rounded-md">Choose files</label>
    <input id="file" type="file" accept=".jpg" bind:files={files} class="custom-file-input" multiple />
  {#if files != undefined}
    <button on:click={uploadFiles} class="text-3xl bg-slate-300 dark:bg-slate-500 dark:hover:bg-blue-500 hover:bg-blue-300 rounded-md p-4 madimi dark:text-white">Upload</button>
    {/if}
    {/if}
    </div>

  <style>
    .custom-file-input {
      width: 0.1px;
      height: 0.1px;
      opacity: 0;
      overflow: hidden;
      position: absolute;
      z-index: -1;
      border-radius: 50%;
    }
    .custom-file-label {
      padding: 10px;
      background-color: #4CAF50; /* Green background */
      color: white; /* White text */
      cursor: pointer; /* Pointer cursor on hover */
    }
    .custom-file-label:hover {
      background-color: #94dd97; /* Darker green background on hover */
    }
  </style>