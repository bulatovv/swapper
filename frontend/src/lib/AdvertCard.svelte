<script>
    export let advert;
</script>

<div class="max-w-sm border border-gray-200 rounded-lg shadow">
    <div class="relative">
        <img class="rounded-t-lg" src="{advert.image}" alt="{advert.title}"/>
        <div class="absolute bottom-5 right-5 p-1 rounded-md text-white bg-gray-900/[0.50]">
            <i class="bi bi-geo-alt-fill"></i>
            {advert.community}
        </div>
    </div>

    <div class="p-5">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">
            {advert.title}
        </h5>
        <p class="mb-3 font-normal text-gray-700 line-clamp-3">
            {advert.description}
        </p>
    </div>
</div>
