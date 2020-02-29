$(document).ready(function () {
    //ф-ия отправки на сервер результатов обучающего теста
    form = $('#form-test');
    var status = false, id_quest, answer, id_answer;
    var url = form.attr("action");
    tmp = false
    //хранит key - вопроса и ответа
    //value - ответ студента

    form.on('submit', function (e) {
        e.preventDefault();
        var data = {};
        var submit_btn = $('#submit_btn');
        var csrf_token = $('#form-test [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        data["test_id"] = $('h2').data("test");

        $("input[type=checkbox]").each(function (index) {
            id_quest = $(this).attr("name");
            id_answer = $(this).attr("id");
            answer = $(this).data("answer");
            status = 'False';
            if ($(this).prop('checked')) {
                status = 'True';
            }
            // data[index] = {key: id_answer, value: status};
            data[index] = {key: id_answer, status: status, quest: id_quest};
        });
        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("SUCCESS");
                const btn = document.querySelector('.btn > span');
                btn.innerHTML = "Результаты успешно отправлены"

                $('#marks').addClass("success-result")
                $('#submit_btn').attr("disabled", true)

            },
            error: function () {
                console.log("ERROR")
            }
        });
    })
});

