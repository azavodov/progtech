document.addEventListener("DOMContentLoaded", () => {
    get_channels()
        .then(() => {
            load_feeds()
        });
});

let OFFSET = 0;
let COUNT = 10;

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
                onChange: () => {
                    OFFSET = 0;
                    document.getElementById("entries_container").innerHTML = "";
                    load_feeds();
                }
            });
            resolve();
        })
    });
}

function load_feeds(){
    document.getElementById('feeds').classList.add("loading");
    let channel_id = $('#channel').dropdown('get value');
    axios.get(`/feeds?c_id=${channel_id}&offset=${OFFSET}&count=${COUNT}`).then(response => {
        document.getElementById('feeds').classList.remove("loading");
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
    })
}
