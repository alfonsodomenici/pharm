import configData from "./../config.js";

const url = `${configData.baseurl}/pharms`;

const findPharm = async (id) => {
    const resp = await fetch(`${url}/${id}/`)
    return resp.json();
}

const updatePharm = async (id, data) => {
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
    return findPharm(id)
}

const removePharm = async (id) => {
    return fetch(`${url}/${id}/`, {
        method: 'DELETE', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached,
    })
}

const boxesByPharm = async (id) => {
    const resp = await fetch(`${url}/${id}/boxes`)
    return resp.json();
}

const createBox = async (id,data) => {
    return fetch(`${url}/${id}/boxes`, {
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

export { findPharm, updatePharm, removePharm, boxesByPharm, createBox };