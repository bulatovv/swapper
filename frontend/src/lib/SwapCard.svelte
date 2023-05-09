<script>
    export let swap;
</script>

<style>
button {
  @apply text-base cursor-pointer px-4 py-1 rounded-[10px] border-2 border-solid my-3;
}

.want-button {
  @apply text-[green] float-right border-[green];
  &:hover {
    @apply bg-[green] text-[white];
  }
}

.not-offer-button {
  @apply text-[red] float-left border-[red];
  &:hover {
    @apply bg-[red] text-[white];
  }
}

.right {
  -webkit-clip-path: polygon(60% 0, 100% 0%, 100% 100%, 40% 100%);
  clip-path: polygon(60% 0, 100% 0%, 100% 100%, 40% 100%);
}

.left {
  position: absolute;
  -webkit-clip-path: polygon(0 0, 60% 0, 40% 100%, 0 100%);
  clip-path: polygon(0 0, 60% 0, 40% 100%, 0 100%);
}
</style>

<div class="max-w-sm border border-gray-200 rounded-lg shadow">
    <div class="relative">
        <img class="rounded-t-lg left" src="{swap.imageF}" alt="{swap.titleF} "/>
        <img class="rounded-t-lg right" src="{swap.imageS}" alt="{swap.titleS} "/>
    </div>

    <div class="p-5">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">
            {swap.titleF} <p> <h5 class="font-normal"> в обмен на </h5> <p> {swap.titleS}
            <p>
            <h5 class="font-normal">
            меняемся с: {swap.user}
            </h5>
        </h5>
        <hr>
        <button class="not-offer-button">Отклонить</button>
        <button class="want-button">Принять</button>
    </div>
</div>
