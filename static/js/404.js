const loader = document.querySelector('.spin_loader');
const page_loader = document.querySelector('.page_loader');

window.addEventListener('load', async () => {
    const tokenMeta = document.querySelector('meta[name="token"]');
    const token = tokenMeta ? tokenMeta.getAttribute('content') : null;

    if (token) {
        localStorage.setItem('token', token);
        tokenMeta.remove();
    } else {
        //
    }

    page_loader.style.display = 'none';
    container.style.display = '';
});