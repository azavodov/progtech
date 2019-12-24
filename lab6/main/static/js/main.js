document.addEventListener("DOMContentLoaded", () => {
    get_channels()
        .then(() => {
            reload_feeds();
        });
});

let OFFSET = 0;
let COUNT = 5;


function new_rss_channel_modal() {
    document.getElementById('new_channel_name').value = "";
    document.getElementById('new_channel_url').value = "";
    $('#add_channel')
        .modal({
            closable: false,
            onApprove: function () {
                add_new_rss_channel();
            }
        })
        .modal('show')
    ;
}

function add_new_rss_channel() {
    let channel_name = document.getElementById('new_channel_name').value;
    let channel_url = document.getElementById('new_channel_url').value;

    axios.get(`/channels/add?name=${channel_name}&url=${channel_url}`)
        .then(response => {
            if (response.data.status === "OK") {
                get_channels();
            } else {
                console.log(response.data.status);
            }
        })
        .catch(error => {
            console.log(error);
        });
}


function get_channels() {
    return new Promise((resolve, reject) => {
        axios.get(`/channels`).then(response => {
            document.getElementById('channel').innerText = "";
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
