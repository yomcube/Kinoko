#include "ObjectBase.hh"

#include <egg/math/Math.hh>

namespace Field {

/// @addr{0x8081F828}
ObjectBase::ObjectBase(const System::MapdataGeoObj &params)
    : m_id(static_cast<ObjectId>(params.id())), m_flags(0x3), m_pos(params.pos()),
      m_rot(params.rot() * DEG2RAD), m_scale(params.scale()), m_transform(EGG::Matrix34f::ident) {}

/// @addr{0x8067E3C4}
ObjectBase::~ObjectBase() = default;

/// @addr{0x808217B8}
void ObjectBase::calcModel() {
    calcTransform();
}

/// @addr{0x80821640}
void ObjectBase::calcTransform() {
    if (m_flags & 2) {
        m_transform.makeRT(m_rot, m_pos);
        m_flags &= ~0x3;
    } else if (m_flags & 1) {
        m_transform.setBase(3, m_pos);
        m_flags |= 4;
    }
}

} // namespace Field
