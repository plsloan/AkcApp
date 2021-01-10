export const AppRoutes = {
    Home: '/home',
    Breeds: '/breeds'
};

export const apiFetch = (path) => fetch(path).then(response => response.json()).then(json => json);