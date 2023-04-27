<script>
	import { getContext } from 'svelte';
	import { TABS } from './Tabs.svelte';

	const tab = {};
	const { registerTab, selectTab, selectedTab } = getContext(TABS);

	registerTab(tab);
</script>

<style> button {
    @apply text-[#ccc] mr-7 m-0 rounded-none border-b-2 border-b-[white] border-[none] border-solid;
    background: none;
}
.selected { @apply text-[#333] border-b-2 border-b-[orange] border-solid; } </style>

<button class:selected="{$selectedTab === tab}" on:click="{() => selectTab(tab)}">
	<slot></slot>
</button>