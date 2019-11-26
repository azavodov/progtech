document.addEventListener("DOMContentLoaded", () => {
    get_channels()
        .then(() => {
            load_feeds()
        });
});

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
                onChange: () => { load_feeds(); }
            });
            resolve();
        })
    });
}

function load_feeds(){
    let channel_id = $('#channel').dropdown('get value');
    axios.get(`/feeds?c_id=${channel_id}`).then(response => {
        let container = document.getElementById('feeds');
        let feeds = response.data['feeds'];
        console.log(feeds);
    })
}
