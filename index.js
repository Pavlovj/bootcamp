    var fs = require('fs');

    var data = {}

    const products = [
        { name: 'bananas', amount: [100, 150], price: 1 },
        { name: 'oranges', amount: [80, 120], price: 3 },
        { name: 'tomatoes', amount: [150, 200], price: 1.5 },
        { name: 'lemons', amount: [80, 100], price: 5 },
        { name: 'grapes', amount: [50, 70], price: 3 },

    ]

    let days = []
    function addWeek(numberOfWeeks, startDate) {
        let days = []
        for (let i = 0; i < numberOfWeeks; i++) {

            for (let j = 0; j < 7; j++) {
                days.push(addDay(startDate));
                startDate.setDate(startDate.getDate() + 1); // increment start date by 1 day
            }
        }

        days = [...days, ...days]
        return days
    }

    function addDay(startDate) {
        let day = {}
        for (let product of products) {
            let amount = products.find(({ name }) => product.name == name).amount
            day[product.name] = {
                date: startDate.toISOString().slice(0, 10),
                amount: randomNumber(amount[0], amount[1]),
                price: product.price
            }
        }
        return day;
    }

    function randomNumber(min, max) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min)
    }

    const startDate = new Date('2022-03-22'); // set start date
    addWeek(52, startDate);

    data.days = days;

    fs.writeFile("input.json", JSON.stringify(data), function (err) {
        if (err) throw err;
        console.log('complete');
    });
