const loader = document.querySelector('.spin_loader');
const page_loader = document.querySelector('.page_loader');
const dlbtn = document.querySelector('.form-submit-btn');
const dllink = document.querySelector('#dllink');
const container = document.querySelector('.form-container');
const form = document.querySelector('.form');
const radio = document.querySelector('.radio-inputs');
var video_content = document.querySelector('.video_content');
var paste_btn = document.querySelector('#paste_clipboard');

async function endpoint_skeleton(link, format_) {
    let site_url = '/';
    const token = localStorage.getItem('token')

    const release_response = await fetch(`${site_url}api/dler`, {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'validation': token
        },
        body: JSON.stringify({
            'link': link,
            'format': format_,
        })
    });

    try {
        if (release_response.ok) {
            const data = await release_response.json();
            if (data) {
                return data;
            }

        } else {
            throw new Error(release_response.status);
        }
    } catch (e) {
        console.error(e);
        return { "url": "https://rr4---sn-ab5sznz6.googlevideo.com/videoplayback?expire=1715393224&ei=aH4-Zvb7BreIkucP_e2pwA8&ip=2604%3Aa880%3A800%3A10%3A0%3A0%3Aa4a%3A7001&id=o-AFqxXZlT0P71t0oaH9iLXw32DFXAn63PEyl8tUXcqgIR&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=u6&mm=31%2C29&mn=sn-ab5sznz6%2Csn-ab5l6nrr&ms=au%2Crdu&mv=m&mvi=4&pl=48&initcwndbps=278750&bui=AWRWj2QgYmHxXGPpHMiVe-y3AJQpQk6lazecH21uBWTvEX_oYTw4lswEHUuiPna1MnhsjFTaml5_nyUk&spc=UWF9f33LlvUinNuXNDL3RCfZDz6F5r_itdYx6AX1JwTVSY770YqwwPM&vprv=1&svpuc=1&mime=video%2Fmp4&ns=MSlLWHraxnsuFH0tw4vrM6sQ&rqh=1&cnr=14&ratebypass=yes&dur=163.213&lmt=1706149439234500&mt=1715371257&fvip=1&c=WEB&sefc=1&txp=4438434&n=q-aPmeZz79uqqg&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRQIhAOpJXoWb4zGDxLdyXH4c5lIhX54GT4KZ04Esqrr-zStQAiA8OUKrTnZHz8cEXGT_yAHGon7Vq77qDZ3dvkXa1l2NTw%3D%3D&sig=AJfQdSswRQIgCoLkhFILtGgiB15PFDOVRfcb9pft74zeinRkZybLHzACIQDTrxlbHdQocDRasOcwZO57K2uZGeoJPYufR9CE0DPYUA%3D%3D", "title": "Vybz Kartel - Hi", "thumbnail": "https://i.ytimg.com/vi/vqOkkVl1hUE/default.jpg" }
    }
}

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

dlbtn.addEventListener('click', async (e) => {
    e.preventDefault();
    var link = dllink.value;

    var radioButtons = document.getElementsByName("radio");

    for (var i = 0; i < radioButtons.length; i++) {

        if (radioButtons[i].checked) {
            var format_ = radioButtons[i].value;
            break;
        }
    }
    if (link !== '') {
        container.style.display = 'none';
        page_loader.style.display = '';
        paste_btn.style.display = '';
        data = await endpoint_skeleton(link, format_);
        if (data) {
            await update_container(data);
            page_loader.style.display = 'none';
            video_content.style.display = '';
        }
    }

});

async function reset_form() {
    document.querySelector('#video_card').remove();
    //video_content.style.display = 'none';
    form.style.display = '';
    container.style.display = '';
}

async function update_container(data) {
    dllink.value = '';
    var div = document.createElement('div');
    var br = document.createElement('br');
    div.className = "content_div";

    if (data['url'] == '#') {
        var dl_link = '#';
        var msg = 'That wasn"t found';
        var dl_btn = `<br>`;
        var dl_more = `Try another`;
        var dl_title = ``;

    } else {
        var msg = `${data['title']}`;
        var dl_btn = `<video
                  controls
                  loop
                  src="${data['url']}"
                  poster="${data['thumbnail']}"
            ></video>`;
        var dl_more = `Download More`;
        var dl_title = ``;
    };

    div.innerHTML = `<div id="video_card" class="card"> 
      <button onclick="reset_form()" class="dismiss" type="button">×</button> 
      <div class="header"> 
        <div class="image">
          <img src="${data['thumbnail']}" alt="download">
          </div> 
          <div class="content">
             <p class="message">${dl_title}</p> 
             </div> 
             <div class="actions">
                ${dl_btn}
                <br>
                <div class="title_div">
                    <span class="title">${msg}</span>
                </div>
                
                <br>
                <button class="track" type="button" onclick="reset_form()">${dl_more}</button> 
                </div> 
                </div> 
                </div>`;

    form.style.display = 'none';
    radio.style.display = 'none';

    video_content.appendChild(div)
    video_content.appendChild(br)
    return div
}