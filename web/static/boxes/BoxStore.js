import configData from "./../config.js";

const url = `${configData.baseurl}/boxes`;

const findBox = async (id) => {
    const resp = await fetch(`${url}/${id}/`)
    return resp.json();
}

const updateBox = async (id, data) => {
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
    return findBox(id)
}

const removeBox = async (id) => {
    return fetch(`${url}/${id}/`, {
        method: 'DELETE', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached,
    })
}


export { findBox, updateBox, removeBox };