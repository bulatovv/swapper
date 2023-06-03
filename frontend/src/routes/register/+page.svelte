<script>
    import { applyAction, deserialize } from '$app/forms';

    
    /** @type {import('./$types').ActionData} */
    export let form;
    
    let email = '';
    let password = '';
    let passwordConfirm = '';

    $: validated = {
        passwordsMatch: !passwordConfirm || passwordConfirm == password,
        get all() {
            return email && passwordConfirm && this.passwordsMatch;
        }
    };

    async function handleSubmit() {
        const data = new FormData();
        data.append('email', email);
        data.append('password', password);

        const response = await fetch(this.action, {
            method: 'POST',
            body: data,
        });

        const result = deserialize(await response.text());
        
        await applyAction(result);
    }
</script>

<div class="flex justify-center items-center">
    <form class="w-1/3 border-[1px] border-gray-400 rounded-lg p-6 shadow-lg" on:submit|preventDefault={handleSubmit}>
        <h1 class="text-4xl font-bold mb-6">Регистрация</h1>
        <label class="text-2xl font-semibold" for="email">Почта</label>
        <input bind:value={email} 
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="email" placeholder="user@example.com" name="email" id="email" required>
        {#if form?.emailExists}
            <p class="text-red-500 text-sm">Этот почтовый адрес уже занят</p>
        {/if}

        <label class="text-2xl font-semibold" for="password">Пароль</label>
        <input bind:value={password} 
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="password" name="password" id="password" required>


        <label class="text-2xl font-semibold" for="password-confirm">Подтвердите пароль</label>
        <input bind:value={passwordConfirm} 
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="password" name="password-confirm" id="password-confirm" required>
        {#if !validated.passwordsMatch}
            <p class="text-red-500 text-sm">Пароли не совпадают</p>
        {/if}


        <div class="flex">
            <button type="submit"
                    disabled={!validated.all}
                    class:bg-gray-400={!validated.all}
                    class="font-bold uppercase trackling-widest bg-orange-400 text-slate-50 rounded-sm p-2 mt-2 ml-auto">
                Зарегистрироваться
                <i class="bi bi-arrow-right font-bold"></i>
            </button>
        </div>
    </form>
</div>
