

const d = new Date();
const weekday={
    "1":"월",
    "2":"화",
    "3":"수","4":"목","5":"금","6":"토","0":"일"
}
const currentDate = d.getFullYear() +"년 "
                    + ( d.getMonth() + 1 ) + "월 " 
                    + d.getDate() + "일 "

const currentDay= weekday[d.getDay()]+"요일";

document.getElementById('current-date').innerHTML = currentDate
document.getElementById('current-day').innerHTML = currentDay

