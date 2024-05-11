var content = document.querySelector("#content");

async function update_page() {
    const token = localStorage.getItem('token')

    let site_url = '/';
    const response = await fetch(`${site_url}api/v1/test`, {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'validation': token
        },
        body: JSON.stringify({
            'link': token,
            'test': 'test',
        })
    });

    try {
        if (response.ok) {
            var data = await response.json();

        } else {
            var data = {"detail": [{"link": "test", "test": "test"}], "all_visits": 1, "unique_visits": 1}
        }
    } catch (e) {
        console.error(e);
    };
    if (data) {
        //content.textContent = '';
        content.textContent = JSON.stringify(data, undefined, 2);   
    };

}

window.addEventListener('load', async () => {
    const tokenMeta = document.querySelector('meta[name="token"]');
    const token = tokenMeta ? tokenMeta.getAttribute('content') : null;

    if (token) {
        localStorage.setItem('token', token);
        tokenMeta.remove();
    } else {
        localStorage.setItem('token', 'token');
        tokenMeta.remove();
    }
    await update_page();
});
