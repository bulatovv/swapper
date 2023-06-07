<script>
    import "../app.css";
    import "bootstrap-icons/font/bootstrap-icons.css";

    import { clickOutside } from '$lib/clickOutside.js'
	import { slide } from 'svelte/transition';
	import { invalidateAll } from '$app/navigation';
    import { applyAction, deserialize } from '$app/forms';


    export let menuExpanded = false;
    
    function toggleMenu() {
        menuExpanded = !menuExpanded;
	}

	function hideMenu() {
		menuExpanded = false;
	}


    async function logout() {
        const res = await fetch("/logout", {
            method: "POST",
            body: new FormData()
        });

        const result = deserialize(await res.text());

        await applyAction(result);
    }

    /** @type {import('./$types').PageData} */
    export let data;
</script>

<header class="flex content-center justify-center sticky top-0 z-30 w-full h-14 px-4 pt-1 pb-2 mb-6 shadow-lg bg-orange-500">
    <div class="flex items-center w-2/3">
        <div class="font-sans font-semibold text-3xl text-slate-100">
			<a href="/">
				<i class="bi bi-repeat"></i>
				<span>Обменус</span>
			</a>
        </div>


		{#if data.user}
			<!-- and new ad button -->
			<button class="text-white bg-purple-600 rounded-md px-2 py-1 ml-auto mr-2">
				<a href="/ads/create">
					<i class="bi bi-plus-circle"></i>
					<span class="ml-2">Новое объявление</span>
				</a>
			</button>

            <div use:clickOutside on:clickOutside="{hideMenu}" class="relative">
                <button on:click="{toggleMenu}" class="text-white bg-orange-400 rounded-md px-2 py-1 mr-2">
                    <i class="bi bi-person-circle"></i>
                    <span class="ml-2">Профиль</span>
                </button>
                {#if menuExpanded}
                    <div transition:slide class="absolute z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-44 mt-2 right-0">
                        <a href="{null}" on:click|preventDefault="{logout}" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900">Выйти</a>
                    </div>
                {/if}
            </div>
        {:else}
            <button class="text-white bg-purple-600 rounded-md px-2 py-1 ml-auto mr-2">
                <a href="/register">
                    <i class="bi bi-person-plus"></i>
                    <span class="ml-2">Зарегистрироваться</span>
                </a>
			</button>
            <button class="text-white bg-orange-400 rounded-md px-2 py-1 mr-2">
                <a href="/login">
                    <i class="bi bi-box-arrow-in-right"></i>
                    <span class="ml-2">Войти</span>
                </a>
			</button>
        {/if}

    </div>
</header>

<main class="flex justify-center">
    <div class="w-2/3">
        <slot/>
    </div>    
</main>

<footer>
</footer>
