<script>
    import AdvertCard from '$lib/AdvertCard.svelte';
    import ReplyCard from '$lib/ReplyCard.svelte';
    import SwapCard from '$lib/SwapCard.svelte';
    import { Tabs, TabList, TabPanel, Tab } from './tabs.js';
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<Tabs>
	<TabList>
		<Tab>Лента предложений</Tab>
		<Tab>Ответить на понравившееся</Tab>
		<Tab>Заключение обмена</Tab>
	</TabList>

	<TabPanel>
    <div class="grid justify-items-center grid-cols-3 gap-y-7">
    {#each data.adverts as advert (advert.id)}
        <AdvertCard advert={advert} />
    {/each}
    </div>
	</TabPanel>

	<TabPanel>
	<div class="grid justify-items-center grid-cols-3 gap-y-7">
    {#each data.replies as reply (reply.id)}
        <ReplyCard reply={reply} />
    {/each}
    </div>
	</TabPanel>

	<TabPanel>
    <div class="grid justify-items-center grid-cols-3 gap-y-7">
    {#each data.swaps as swap (swap.id)}
        <SwapCard swap={swap} />
    {/each}
    </div>
	</TabPanel>
</Tabs>