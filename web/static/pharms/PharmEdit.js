import { html, render } from "./../lib/lit-html.js";
import { Router } from "./../lib/vaadin-router.js";
import { router } from "./../index.js";
import { findPharm, updatePharm } from "./pharmStore.js";
import { createPharm } from "./../users/userStore.js";
import configData from "./../config.js";

export default class PharmEdit extends HTMLElement {

    constructor() {
        super();
    }

    getRoot() {
        return this;
    }

    connectedCallback() {
        const { location } = router;
        this.id = location.params.pharm;
        if (this.id == "undefined") {
            console.log("create..")
            this.data = {
                name:'',
                macaddress:'',
                accesspoint:'',
                password:'',
                ip:'' ,
                wiocode:'',
                gmt:''   
            }
            render(this.renderView(), this.getRoot());
        } else {
            findPharm(this.id)
                .then(data => {
                    this.data = data;
                    render(this.renderView(), this.getRoot());
                })
        }

    }

    onInputChange(e) {
        const { name, value } = e.target;
        this.data[name] = value;
    }

    onSave(e) {
        e.preventDefault();
        const {form} = e.target;
        if(!form.checkValidity()){
            form.reportValidity();
            return;
        }
        if (this.id === "undefined") {
            createPharm(configData.userId, this.data)
                .then(_ => {
                    Router.go(`/pharms/`);
                })
        } else {
            updatePharm(this.id, this.data)
                .then(_ => {
                    Router.go(`/pharms/`);
                })
        }

    }

    onCancel(e) {
        e.preventDefault();
        Router.go(`/pharms/`);
    }

    renderView() {
        return html`
           <form>
                <div class="field">
                    <label class="label">Nome</label>
                    <div class="control">
                        <input required class="input" type="text" @change=${e => this.onInputChange(e)} name="name" .value=${this.data.name} placeholder="nome...">
                    </div>
                </div>
                
                <div class="field">
                    <label class="label">Macaddress</label>
                    <div class="control">
                        <input required class="input" type="text" name="macaddress" @change=${e => this.onInputChange(e)} .value=${this.data.macaddress} placeholder="mac address...">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Acccess Point</label>
                    <div class="control">
                        <input required class="input" type="text" name="accesspoint" @change=${e => this.onInputChange(e)} .value=${this.data.accesspoint} placeholder="access point...">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Pasword</label>
                    <div class="control">
                        <input required class="input" type="password" name="password" @change=${e => this.onInputChange(e)} .value=${this.data.password} >
                    </div>
                </div>

                <div class="field">
                    <label class="label">IP</label>
                    <div class="control">
                        <input required class="input" type="text" name="ip" @change=${e => this.onInputChange(e)} .value=${this.data.ip} placeholder="ip address...">
                    </div>
                </div>

                <div class="field">
                    <label class="label">wiocode</label>
                    <div class="control">
                        <input required class="input" type="text" name="wiocode" @change=${e => this.onInputChange(e)} .value=${this.data.wiocode} placeholder="wiocode...">
                    </div>
                </div>

                <div class="field">
                    <label class="label">gmt</label>
                    <div class="control">
                        <input required class="input" type="text" name="gmt" @change=${e => this.onInputChange(e)} .value=${this.data.gmt} placeholder="gmt...">
                    </div>
                </div>

                <div class="field is-grouped">
                    <div class="control">
                        <button class="button is-link" @click = ${e => this.onSave(e)}>Save</button>
                    </div>
                    <div class="control">
                        <button class="button is-link is-light" @click = ${e => this.onCancel(e)}>Cancel</button>
                    </div>
                </div>
           </form>
        `;
    }
}
customElements.define("pharm-edit", PharmEdit);