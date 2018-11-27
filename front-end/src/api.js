import { create } from 'apisauce';

const URL = 'https://tweemotion-back.herokuapp.com';

const api = create({
    baseURL: URL,
    headers: { 
        'Access-Control-Allow-Origin': "*",
        'Content-Type': 'application/json' 
    }
});

export {
    api
};