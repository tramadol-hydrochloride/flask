const API_URL = 'http://localhost:5000/api';

const display_json = (query) => {

    d3.json(API_URL + query)
        .then((data) => {
            d3.select('#query pre').html(query);
            d3.select('#data pre').html(JSON.stringify(data, null, 4));
            console.log(data);
        })
        .catch((error) => console.warn(error));
};

// const query = '/winners?where=' + JSON.stringify({
//     "year": {"$gt":2000},
//     "gender": "female"
// });

// const query = '/winners?projection=' + JSON.stringify({
//     'mini_bio': 0
// });

const query = '/winners?where=' + JSON.stringify({
    'name': 'Albert Einstein'
});

display_json(query);
