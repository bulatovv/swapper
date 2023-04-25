<script>
    import "../app.css";
    import "bootstrap-icons/font/bootstrap-icons.css";
</script>

<header class="flex content-center justify-center sticky top-0 z-30 w-full h-14 px-4 pt-1 pb-2 mb-6 shadow-lg bg-orange-500">
    <div class="flex items-center w-2/3">
        <div class="font-sans font-semibold text-4xl text-slate-100">
            <i class="bi bi-repeat"></i>
            Обменус
        </div>
        <div class="font-sans font-semibold text-2xl text-slate-100 ml-auto ">
            Вход
        </div>
    </div>
</header>

<main class="flex justify-center">
    <div class="w-2/3">
        <slot/>
    </div>    
</main>

<footer>
</footer>
