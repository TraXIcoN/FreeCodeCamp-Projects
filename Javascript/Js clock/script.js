
        const secondHand = document.querySelector('.second-hand');
        const minHand = document.querySelector('.min-hand');
        const hourHand = document.querySelector('.hour-hand');
        const digital = document.querySelector('.digital');
        function setDate(){

            

        const now = new Date();
        const day = now.getDay();
            const daylist = ["Sunday", "Monday", "Tuesday", 
                        "Wednesday", "Thursday", "Friday", 
                        "Saturday"]
            console.log("Today is " + daylist[day] + ".")

        const seconds = now.getSeconds();
        const secondDegree = ((seconds / 60) * 360 + 90) ;
        secondHand.style.transform =`rotate(${secondDegree}deg)`;
        
        const minutes = now.getMinutes();
        const minuteDegree = ((minutes / 60) * 360 + 90) ;
        minHand.style.transform =`rotate(${minuteDegree}deg)`;
        
        const hours = now.getHours();
        const hourDegree = ((hours / 12) * 360 + 90) ;       
        hourHand.style.transform =`rotate(${hourDegree}deg)`;
        var ampm = "AM";
        if(hours < 12){
            ampm = "AM";
        }
        if(hours >= 12){
            
            ampm = "AM";
        }
            if(seconds < 10){
                seconds = "0"+ seconds;
            }
            
            if(minutes < 10){
                minutes = "0"+ minutes;
            }
            document.getElementById('date').innerHTML = daylist[day];
            digital.innerHTML = hours +" : "+ minutes +" : "+seconds;
        
}

setInterval(setDate,1000);