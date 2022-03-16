const DocLink = async () => {
    a = document.getElementById('fileLink');
    
    a.href = "{{ url_for('static',filename='Abstracts/1.txt') }}"
}