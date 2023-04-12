<script>
    import AdvertCard from '$lib/AdvertCard.svelte';

    /** @type {import('./$types').PageData} */
    export let data;
</script>


{#each data.adverts as advert (advert.id)}
    <AdvertCard advert={advert} />
{/each}
