export * as breedData from './data.json';

export const AppRoutes = {
    Home: '/home',
    Breeds: '/breeds',
    BreedSearch: '/breed-search'
};

export const apiFetch = (path) => fetch(path).then(response => response.json()).then(json => json);
