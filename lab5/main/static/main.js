document.addEventListener("DOMContentLoaded",  () => {

    $('.ui.dropdown').dropdown();
    generate_game();

});

let ANSWER;


function generate_game() {
    document.getElementById("answer").innerText = "";
    document.getElementById("result").innerText = "";

    let level = $("#level").dropdown('get value');
    let max_id = 10;
    switch (level) {
        case 0:
            max_id = 10;
            break;
        case 1:
            max_id = 50;
            break;
        case 2:
            max_id = 100;
            break;
    }
    get_photo(max_id);
    get_names(max_id);
}

function check_answer(){
    let user_answer = $("#user_answer").dropdown('get value');
    document.getElementById("answer").innerText = ANSWER['name'];
    let result = document.getElementById("result");
    console.log(user_answer, ANSWER['id']);
    if (user_answer == ANSWER['id']){
        result.innerText = 'Верно!';
    } else {
        result.innerText = 'Вы ошиблись!';
    }
}

function get_photo(max_id){
    axios.get(`/get/photo/${max_id}`).then(response => {
        let container = document.getElementById('photo');
        ANSWER = response.data.name;
        container.src = response.data.photo;
    })
}

function get_names(max_id){
    axios.get(`/get/names/${max_id}`).then(response => {
        let container = document.getElementById('user_answer_container');
        container.innerHTML = `<select class="ui fluid search dropdown" onchange="check_answer()" id="user_answer"></select>`;
        let names = response.data.names;
        if (!names.filter(name => name['id'] === ANSWER['id']).length){
            names.pop();
            names.push(ANSWER);
        }
        names = names.sort(() => { return Math.random() - 0.5; });
        $.each(names, (name) => {
            $('#user_answer')
                .append($("<option></option>")
                    .attr("value", names[name]['id'])
                    .text(names[name]['name']));
        });
        $('#user_answer').dropdown();
    })
}