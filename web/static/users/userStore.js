import configData from "./../config.js";

const url = `${configData.baseurl}/users`;
const allUsers = async () => {
    const resp = await fetch(`${url}/`)
    return resp.json();
}

const findUser = async (id) => {
    const resp = await fetch(`${url}/${id}/`)
    return resp.json();
}

const updateUser = async (id, data) => {
    const resp = await fetch(`${url}/${id}/`, {
        method: 'PATCH', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached,
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data)
    })
    return findUser(id)
}

const createUser = async (data) => {
    return fetch(`${url}/`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached,
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data)
    })
}

const removeUser = async (id) => {
    return fetch(`${url}/${id}/`, {
        method: 'DELETE', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached,
    })
}

const pharmsByUser = async (id) => {
    const resp = await fetch(`${url}/${id}/pharms`)
    return resp.json();
}

const createPharm = async (id,data) => {
    return fetch(`${url}/${id}/pharms`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached,
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data)
    })
}
export { allUsers, findUser, createUser, updateUser, removeUser, pharmsByUser, createPharm };