<script>
    import { applyAction, deserialize } from '$app/forms';
    import slugify from 'slugify';
    
    /** @type {import('./$types').PageData} */
    export let data;


    let title = '';
    let description = '';
    let imgUrl = '';

    let filepicker;
    let imgPreview = 'https://via.placeholder.com/640x360.png?text=Image+preview';

    async function uploadImage() {
        const file = this.files[0];
        const reader = new FileReader();

        reader.onload = function(e) {
            imgPreview = e.target.result;
        }

        reader.readAsDataURL(file);

        const fileExtension = file.name.split('.').pop();
        let filename;
        if (title) {
            filename = slugify(title, { lower: true }) + '.' + fileExtension;
        } else {
            filename = file.name;
        }


        const form = new FormData();
        form.append('image', file, filename);


        const response = await fetch('/images', {
            method: 'POST',
            body: form,
        });

        imgUrl = (await response.json())['image_url'];
    }

    async function handleSubmit() {
        const form = new FormData();
        form.append('title', title);
        form.append('description', description);
        form.append('image_url', imgUrl);
        form.append('user_id', data.user.id);

        const response = await fetch(this.action, {
            method: 'POST',
            body: form,
        });

        const result = deserialize(await response.text());

        await applyAction(result);
    }
</script>

<div class="flex justify-center items-center">
    <input bind:this="{filepicker}" on:change="{uploadImage}" class="hidden" type="file" accept="image/*" />
    

    <form class="w-1/3 border-[1px] border-gray-400 rounded-lg p-6 shadow-lg" on:submit|preventDefault={handleSubmit}>
        <h1 class="text-4xl font-bold mb-6">Создать объявление</h1>

        <img on:click="{() => filepicker.click()}" class="w-full mb-2" src={imgPreview}/> 
 

        <label class="text-2xl font-semibold" for="title">Название</label>
        <input bind:value={title}
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="text" placeholder="Гречка" name="title" id="title" required>

        <label class="text-2xl font-semibold" for="description">Описание</label>
        <input bind:value={description}
               class="w-full rounded-md border-[1px] border-gray-400 px-1 py-1 mb-2"
               type="text" placeholder="Вкуснейшая" name="description" id="description" required>
        
        <div class="flex">
            <button type="submit"
                    class="font-bold uppercase trackling-widest bg-orange-400 text-slate-50 rounded-sm p-2 mt-2 ml-auto">
                опубликовать
                <i class="bi bi-arrow-right font-bold"></i>
            </button>
        </div>
    </form>
</div>
