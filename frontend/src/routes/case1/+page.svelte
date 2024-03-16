<script>
  let files;
  let imageUrls = [];

  const uploadFiles = async () => {
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
  };

  function repeat() {
    imageUrls = [];
  }
</script>

<h1 class="dark:text-white text-9xl mt-10 madimi">Solution 1</h1>

{#if imageUrls && imageUrls.length > 0}
  {#each imageUrls as imageUrl}
    <img src={imageUrl} alt="Uploaded image" class="h-auto" style="width: 300px" />
  {/each}

  <button on:click={repeat} class="cu">Try Again</button>
{:else}
  <label for="file" class="custom-file-label">Choose folder</label>
  <input id="file" type="file" webkitdirectory bind:files={files} class="custom-file-input" />

  <button on:click={uploadFiles} class="text-3xl bg-slate-300 dark:bg-slate-500 dark:hover:bg-blue-500 hover:bg-blue-300 rounded-md p-4 madimi dark:text-white">Upload</button>
{/if}