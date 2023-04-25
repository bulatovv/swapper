<script>
    import AdvertCard from '$lib/AdvertCard.svelte';

    /** @type {import('./$types').PageData} */
    export let data;
</script>

<div class="grid justify-items-center grid-cols-3 gap-y-7">
    {#each data.adverts as advert (advert.id)}
        <AdvertCard advert={advert} />
    {/each}
</div>
