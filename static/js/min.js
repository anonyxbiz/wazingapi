window.addEventListener('load', async () => {
    const tokenMeta = document.querySelector('meta[name="token"]');
    const token = tokenMeta ? tokenMeta.getAttribute('content') : null;

    if (token) {
        localStorage.setItem('token', token);
        tokenMeta.remove();
    } else {
        //
    }

});
