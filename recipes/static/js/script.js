
/*
function Data() {
 
    const data = new Date()

    
    function zeroEsquerda(num) {
        return num >= 10 ? num : `0${num}`
    }

    function getDay(data) {
        const day = zeroEsquerda(data.getDate())
        return day
    }
    
    function getMonth(data){
        const month = zeroEsquerda(data.getMonth()+1)
        return month
    }

    function getYear(data){
        const year = zeroEsquerda(data.getFullYear())
        return year
    }
    const documento = document.querySelectorAll('.date')
    
    documento.forEach((date, num) =>{
        date.innerHTML = `<p>${getDay(data)}/${getMonth(data)}/${getYear(data)}</p>`
    })

}
Data()*/