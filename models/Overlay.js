const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const overlaySchema = new Schema({
    type: {
        type: String, // "text" or "image"
        required: true,
        enum: ["text", "image"]
    },
    content: {
        type: String, // The actual text or the image URL
        required: true
    },
    position: {
        x: { type: Number, required: true }, // Horizontal coordinate
        y: { type: Number, required: true }  // Vertical coordinate [cite: 24]
    },
    size: {
        width: { type: Number, required: true },  // Width in pixels
        height: { type: Number, required: true } // Height in pixels [cite: 25]
    }
}, { timestamps: true });

module.exports = mongoose.model('Overlay', overlaySchema);
