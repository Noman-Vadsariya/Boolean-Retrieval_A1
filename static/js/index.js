
const redirect = async(event) => {
    $.form.on('submit',function(event){
        event.preventDefault();
        console.log($('#query').val())
        $.ajax({
            data: {"Query":$('#query').val()},
            type: 'POST',
            url: '/results'

        })
        .done(function(data){
            console.log(data)
        })

        
    });
}