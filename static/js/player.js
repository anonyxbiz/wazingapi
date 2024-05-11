
paste_btn.addEventListener('click', async () => {
    dllink.value = 'pasting from clipboard...';
    try {
        const clip_content = await navigator.clipboard.readText();
        dllink.value = '';
        dllink.value = clip_content;
        paste_btn.style.display = 'none';
        
    } catch (err) {
        var msg = `Failed to read clipboard contents`;
        console.error(`${msg}: `, err);
        dllink.value = msg;
    }
   
});