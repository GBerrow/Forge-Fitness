// Import only the specific Bootstrap components we need for better performance
import { Dropdown } from 'bootstrap';
import { Collapse } from 'bootstrap';

// Wait for the DOM to be fully loaded before initializing components
document.addEventListener('DOMContentLoaded', function() {
    // Find all elements with dropdown-toggle class and initialize Bootstrap dropdowns
    var dropdowns = document.querySelectorAll('.dropdown-toggle');
    dropdowns.forEach(function(dropdown) {
        // Create new Dropdown instance for each element
        new Dropdown(dropdown);
    });
    
    // Find all elements with data-bs-toggle="collapse" attribute and initialize Bootstrap collapsibles
    var collapses = document.querySelectorAll('[data-bs-toggle="collapse"]');
    collapses.forEach(function(collapse) {
        // Create new Collapse instance for each element
        new Collapse(collapse);
    });
});