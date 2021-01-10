import * as breedDataJson from './data.json';

export const apiFetch = (path) => fetch(path).then(response => response.json()).then(json => json);

export const AppRoutes = {
    Home: '/home',
    Breeds: '/breeds',
    BreedSearch: '/breed-search'
};

Object.keys(breedDataJson).map(k => console.log(k));

export const breedData = JSON.parse(breedDataJson);
