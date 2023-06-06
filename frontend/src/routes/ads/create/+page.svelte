<script>
    let name = '';
    let description = '';
    let img = '';
    let adress = '';
    function handleSubmit() {
    }
</script>

<div class="flex justify-center items-center">
    <form class="w-1/3 border-[1px] border-gray-400 rounded-lg p-6 shadow-lg" on:submit|preventDefault={handleSubmit}>
        <h1 class="text-4xl font-bold mb-6">Создать объявление</h1>
        <label class="text-2xl font-semibold" for="name">Название</label>
        <input bind:value={name}
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="name" placeholder="Гречка" name="name" id="email" required>

        <label class="text-2xl font-semibold" for="description">Описание</label>
        <input bind:value={description}
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="description" placeholder="Вкуснейшая" name="description" id="description" required>

        <label class="text-2xl font-semibold" for="img">URL</label>
        <input bind:value={img}
                class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
                type="img" placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ" name="img" id="img" required>
        
        <label class="text-2xl font-semibold" for="img">Ваш адрес</label>
        <input bind:value={adress}
                class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
                type="adress" placeholder="123 квартира" name="adress" id="adress" required>

        <div class="flex">
            <button type="submit"
                    class="font-bold uppercase trackling-widest bg-orange-400 text-slate-50 rounded-sm p-2 mt-2 ml-auto">
                опубликовать
                <i class="bi bi-arrow-right font-bold"></i>
            </button>
        </div>
    </form>
</div>
