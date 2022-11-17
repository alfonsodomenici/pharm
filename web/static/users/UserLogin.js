import { html, render } from "./../lib/lit-html.js";
import { Router } from "./../lib/vaadin-router.js";
import { login } from "./authStore.js";

export default class UserLogin extends HTMLElement {

    constructor() {
        super();
    }

    getRoot() {
        return this;
    }

    connectedCallback() {
        console.log('connected callback')
        this.data = {
            'usr': '',
            'pwd': ''
        }
        render(this.renderView(), this.getRoot());
    }

    onInputChange(e) {
        const { name, value } = e.target;
        this.data[name] = value;
    }

    onLogin(e) {
        e.preventDefault();
        const { form } = e.target;
        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }

        login(this.data)
            .then(payload => {
                console.log(payload)
            })
    }

    onCancel(e) {
        e.preventDefault();
        Router.go(`/`);
    }
    renderView() {
        return html`
           <form>
                <div class="field">
                    <label class="label">Username</label>
                    <div class="control">
                        <input required class="input" type="text" @change=${e => this.onInputChange(e)} name="usr" .value=${this.data.usr} placeholder="username...">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Password</label>
                    <div class="control">
                        <input required class="input" type="password" name="pwd" @change=${e => this.onInputChange(e)} .value=${this.data.pwd} >
                    </div>
                </div>

                <div class="field is-grouped">
                    <div class="control">
                        <button class="button is-link" @click = ${e => this.onLogin(e)}>Login</button>
                    </div>
                    <div class="control">
                        <button class="button is-link is-light" @click = ${e => this.onCancel(e)}>Cancel</button>
                    </div>
                </div>
           </form>
        `;
    }
}
customElements.define('user-login', UserLogin);