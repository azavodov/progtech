document.addEventListener("DOMContentLoaded", () => {
    get_channels()
        .then(() => {
            reload_feeds();
        });
});

let OFFSET = 0;
let COUNT = 5;

function get_channels() {
    return new Promise((resolve, reject) => {
        axios.get(`/channels`).then(response => {
            let channels = response.data['channels'];
            $.each(channels, (channel) => {
                $('#channel')
                    .append($("<option></option>")
                        .attr("value", channels[channel]['id'])
                        .text(channels[channel]['name']));
            });
            $('#channel').dropdown({
                onChange: () => { reload_feeds(); }
            });
            resolve();
        })
    });
}

function reload_feeds() {
    OFFSET = 0;

    let container = document.getElementById('reload_button');
    container.classList.add("loading");

    document.getElementById("entries_container").innerHTML = "";
    load_feeds().finally(() => {
        container.classList.remove("loading");
    });
}

function load_feeds() {
    return new Promise((resolve, reject) => {
        let load_button = document.getElementById('load_button');
        load_button.classList.add('loading');

        let channel_id = $('#channel').dropdown('get value');
        axios.get(`/feeds?c_id=${channel_id}&offset=${OFFSET}&count=${COUNT}`).then(response => {
            load_button.classList.remove('loading');
            let container = document.getElementById('entries_container');

            let feeds = response.data['feeds'];
            for (let i in feeds) {
                container.innerHTML += `
                    <div class="item"">
                        <div class="content">
                          <a class="header" href="${feeds[i]['link']}" target="_blank">${feeds[i]['title']}</a>
                          <div class="meta">
                            <span class="cinema">${feeds[i]['published_time']}</span>
                          </div>
                          <div class="description">
                            ${feeds[i]['description']}
                          </div>
                        </div>
                    </div>
                `;
            }

            OFFSET += COUNT;
            resolve();
        })

    });
}
