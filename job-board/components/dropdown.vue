<template>
    <select 
        v-model="selectedValue"
        @change="$emit('update:modelValue', selectedValue)"
        class="w-full px-4 py-4 bg-gray-100 dark:bg-gray-800 dark:text-gray-500 dark:placeholder-gray-600 rounded-md focus:outline-none focus:ring focus:ring-indigo-300"
    >
        <option value="" disabled>{{ placeholder }}</option>
        <option 
            v-for="option in options" 
            :key="option.id" 
            :value="option.id"
        >
            {{ option.title }}
        </option>
    </select>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
    modelValue: {
        type: [String, Number],
        default: ''
    },
    options: {
        type: Array,
        required: true
    },
    placeholder: {
        type: String,
        default: 'Select an option'
    }
});

const selectedValue = ref(props.modelValue);
</script>