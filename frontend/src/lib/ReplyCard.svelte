<script>
    export let reply;
</script>

<style>
button {
  @apply text-base cursor-pointer px-4 py-1 rounded-[10px] border-2 border-solid my-3;
}

.want-button {
  @apply text-[green] float-right border-[green];
}

.not-offer-button {
  @apply text-[red] float-left border-[red];
}
</style>

<div class="max-w-sm border border-gray-200 rounded-lg shadow">
    <div class="relative">
        <img class="rounded-t-lg" src="{reply.image}" alt="{reply.title}"/>
        <div class="absolute bottom-5 right-5 p-1 rounded-md text-white bg-gray-900/[0.50]">
            <i class="bi bi-geo-alt-fill"></i>
            {reply.community}
        </div>
    </div>

    <div class="p-5">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">
            {reply.title}
            <p>
            author: {reply.user}
        </h5>
        <p class="mb-3 font-normal text-gray-700 line-clamp-3">
            {reply.description}
        </p>
        <hr>
        <button class="not-offer-button">Ничего не понравилось</button>
        <button class="want-button">Выбрать понравившееся</button>
    </div>
</div>
