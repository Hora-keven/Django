

function Tudo() {
 
    const data = new Date()
    let diadasemana = data.getDay()

    function zeroEsquerda(num) {
        return num >= 10 ? num : `0${num}`
    }

    function getDay(data) {
        const day = zeroEsquerda(data.getDate())
        return day
    }
    
    function getMonth(data){
        const month = zeroEsquerda(data.getMonth())
        return month
    }

    function getYear(data){
        const year = zeroEsquerda(data.getFullYear())
        return year
    }
    document.querySelector('.date').innerHTML = `<p>${getDay(data)}/${getMonth(data)}/${getYear(data)}</p>`
}
Tudo()